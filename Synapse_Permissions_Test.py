from azure.synapse.artifacts import ArtifactsClient
from azure.identity import ClientSecretCredential
from azure.identity import DefaultAzureCredential



if __name__ == "__main__":

    # the name of the workspace
    workspace_name = "lakehouseworkspace"

    # the name of the pipeline to be triggered (P.S.: this pipeline should be a test pipeline that doesn't incur any costs)
    pipeline_name = "Google Troubleshooting Pipeline"

    # the three parameters obtained after creating the service principal
    tenant_id="" # your tenant id
    client_id="" #  your client id
    client_secret="" # your client secret








    # decide which login method to use based on the information entered by the user
    if tenant_id!="" and client_id!="" and client_secret!="":
        # log in using a service principal
        service_principal_credential = ClientSecretCredential(
            tenant_id=tenant_id, # your tenant id
            client_id=client_id, #  your client id
            client_secret=client_secret, # your client secret
        )
        client = ArtifactsClient(service_principal_credential,f"https://{workspace_name}.dev.azuresynapse.net")
    else:
        # log in using the credentials on the system (i.e., using the credentials used for configuring the Azure CLI)
        cli_credentials = DefaultAzureCredential()
        client = ArtifactsClient(cli_credentials,f"https://{workspace_name}.dev.azuresynapse.net")


    # creates a pipeline run (i.e., triggers a pipeline)
    response = client.pipeline.create_pipeline_run(pipeline_name)
    print(response)
    run_id = response.run_id
    print("pipeline started with run_id: ", run_id)

    # check status of a pipeline
    response= client.pipeline_run.get_pipeline_run(run_id)

    print(f"the current status of the pipeline run with run_id: {run_id} is {response.status}")
