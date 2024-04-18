import boto3

ec2 = boto3.client('ec2')

def launch_instance():
    
    instance_name = input("Enter instance name: ")

    instance = ec2.run_instances(
        ImageId='ami-007020fd9c84e18c7', 
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )

    instance_id = instance['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} with name '{instance_name}' launched successfully!")

def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} stopped successfully!")

def terminate_instance(instance_id):
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} terminated successfully!")

def main():
    while True:
        print("\nMenu:")
        print("1. Launch Instance")
        print("2. Stop Instance")
        print("3. Terminate Instance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            launch_instance()
        elif choice == '2':
            instance_id = input("Enter instance ID to stop: ")
            stop_instance(instance_id)
        elif choice == '3':
            instance_id = input("Enter instance ID to terminate: ")
            terminate_instance(instance_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
