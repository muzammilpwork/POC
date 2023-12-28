import subprocess

# Define the command as a single string with a shell separator (&&).
cmd = 'echo "I like potatoes" && pwd'

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

o, e = proc.communicate()

print('Output: ' + o.decode('ascii'))
print('Error: ' + e.decode('ascii'))
print('Exit Code: ' + str(proc.returncode))
str(o.decode('ascii')).split('\n')



import configparser


print("Welcome to POC app of odoo deployement using Docker")
print("Please below option to proceed...")
print("1 Custom odoo app")
print("2 Custom odoo modules")
method = input("Enter your option: ")

print(method)

if str(method) == 1:
    odoo_app_path = input("Enter your odoo app path: ")
    odoo_app_config_path = input("Enter your odoo config file path: ")
    config = configparser.ConfigParser()
    config.read(odoo_app_config_path)
    addons_path = config.get('options', 'addons_path')
    addons_path_list = addons_path.split(',')
    if str(addons_path_list[0]).endswith('addons'):
        pass
    
    print("Creating new Docker image for your odoo application...")
    # Define the Dockerfile content
    dockerfile_content = f"""\
    # Use the official Odoo base image
    FROM odoo:14

    # Set the maintainer label
    LABEL maintainer="Name"

    # Set the working directory to /mnt/extra-addons
    WORKDIR /mnt/extra-addons

    # Copy your custom Odoo module to the container
    COPY {odoo_app_path}/addons /mnt/extra-addons

    # Expose the Odoo service port
    EXPOSE 8069

    # Start Odoo
    CMD ["odoo"]
    """

    # Define the file path for the Dockerfile
    dockerfile_path = "Dockerfile"

    # Write the Dockerfile content to the file
    with open(dockerfile_path, "w") as dockerfile:
        dockerfile.write(dockerfile_content)

    print(f"Created Dockerfile at {dockerfile_path}")
    




import configparser

# Define the path to your odoo.conf file
config_file = '/Odoo/odoo/debian/odoo.conf'  # Replace with the actual path to your odoo.config file

# Create a ConfigParser object and read the configuration file
config = configparser.ConfigParser()
config.read(config_file)

# Get the value of addons_path from the [options] section
addons_path = config.get('options', 'addons_path')

print(addons_path)
