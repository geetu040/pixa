# configmap.yaml
- It contains all the evironmental variables and secrets for
	- Azure Database for MySQL flexible server
	- Azure Storage Account File Service
	- Azure Storage Account Blob Service
	- JWT Token Secrets
- These config values are available to containers as environmental variable

# storageclass.yaml
- It creates a share in Azure Storage Account File Service, providing a persistent volume
- This volume is accessable from Azure Portal and can be mounted in containers and VMs

# persistentvolumeclaim.yaml
- This creates a claim on persistent storage created using StorageClass
- This claim is referred in containers and deployments to mount origial storage

# service.yaml
- It map Node's public IP address to deployment
- It balances load between different replicas of deployment

# deployment.yaml
- It creates 3 replicas of Pod, thus providing backup on failure of one pod and also enable load balancing
- Each pod defines 5 containers which are running on different ports and communicating using localhost