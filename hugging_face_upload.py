from huggingface_hub import HfApi, login, create_repo
api = HfApi()

token = input("token: ")
repo_name = input("repo name: ")

login(token=token)

create_repo(f"hegasz/{repo_name}", private=True)

api.upload_folder(
    folder_path="/ai-economist/tutorials/rllib/phase2",
    repo_id=f"hegasz/{repo_name}",
    repo_type="model",
)