import os
import json
import re
from datetime import datetime

# Get the current directory
base_dir = os.path.dirname(os.path.abspath(__file__))

def get_workflow_name(directory):
    """Extract workflow name from directory name"""
    return directory.replace('-', ' ').title()

def get_workflow_json(workflow_dir):
    """Find and load the workflow JSON file"""
    for file in os.listdir(workflow_dir):
        if file.endswith('.json'):
            with open(os.path.join(workflow_dir, file), 'r') as f:
                return json.load(f)
    return None

def generate_documentation(workflow_name, workflow_json):
    """Generate documentation from template and workflow JSON"""
    # Basic workflow info
    description = workflow_json.get('description', 'No description available')
    
    # Extract nodes information
    nodes = workflow_json.get('nodes', [])
    
    # Generate configuration section
    config_section = "## 🛠 Configuration\n\n### Workflow Parameters\n"
    
    # Find parameters from webhook or http request nodes
    parameters = []
    for node in nodes:
        if node.get('type') in ['n8n-nodes-base.webhook', 'n8n-nodes-base.httpRequest']:
            params = node.get('parameters', {})
            for key, value in params.items():
                if isinstance(value, str) and value.strip() and key not in ['url', 'authentication']:
                    parameters.append({
                        'name': key,
                        'type': 'string',
                        'required': 'Yes' if node.get('required') else 'No',
                        'default': str(value) if value else '-',
                        'description': f'From {node.get("name", "unnamed")} node'
                    })
    
    # Add parameters to config section
    if parameters:
        config_section += "| Parameter | Type | Required | Default | Description |\n"
        config_section += "|-----------|------|----------|---------|-------------|\n"
        for param in parameters:
            config_section += f"| {param['name']} | {param['type']} | {param['required']} | {param['default']} | {param['description']} |\n"
    else:
        config_section += "No configurable parameters found.\n"
    
    # Generate node-specific settings
    config_section += "\n### Node-Specific Settings\n"
    for node in nodes:
        if node.get('type') not in ['n8n-nodes-base.start', 'n8n-nodes-base.merge']:
            node_name = node.get('name', 'Unnamed Node')
            node_type = node.get('type', 'Unknown')
            config_section += f"- **{node_name}** ({node_type}):\n"
            
            # Safely get parameters
            params = node.get('parameters', {})
            if isinstance(params, dict):
                for key, value in params.items():
                    if key not in ['url', 'authentication'] and value and not key.startswith('_'):
                        try:
                            value_str = str(value)
                            if len(value_str) > 100:
                                value_str = value_str[:100] + '...'
                            config_section += f"  - `{key}`: {value_str}\n"
                        except Exception as e:
                            config_section += f"  - `{key}`: [Complex value]\n"
    
    # Generate monitoring section with execution info
    monitoring_section = "## 🔍 Monitoring & Maintenance\n\n### Logging\n- Logs can be viewed in the n8n Executions tab\n- Each execution includes detailed logs for debugging\n\n### Performance Metrics\n- Average execution time: [Add expected time]\n- Memory usage: [Add expected usage]\n"
    
    # Generate version history
    version_section = "## 🔄 Version History\n\n| Version | Date       | Changes                     |\n|---------|------------|----------------------------|\n| 1.0.0   | " + datetime.now().strftime("%Y-%m-%d") + " | Initial release             |\n"
    
    # Combine all sections
    documentation = f"""# {workflow_name}

## 📋 Overview
{description}

## 🚀 Quick Start

### Prerequisites
- n8n instance (v1.0+ recommended)
- [List any specific requirements]

### Installation
1. **Import Workflow**
   - Download the workflow JSON file
   - In n8n, go to Workflows → Import from File
   - Select the downloaded JSON file

2. **Configure Credentials**
   - [List required credentials and how to set them up]
   - Example: API keys, database connections, etc.

3. **Environment Variables**
   ```env
   # Copy these to your .env file
   VARIABLE_NAME=value
   ```

{config_section}

## 🏃‍♂️ Running the Workflow

### Manual Execution
1. Open the workflow in n8n
2. Click "Execute Node" on the trigger node
3. Monitor execution in the "Executions" tab

### Scheduled Execution
- **Cron Expression**: `0 * * * *` (runs every hour)
- Adjust the cron expression as needed

## 📊 Expected Output

### Successful Execution
- Description of successful output
- Example response:
  ```json
  {{
    "status": "success",
    "data": {{}}
  }}
  ```

### Error Handling
- Common error messages and resolutions
- How to interpret error codes

{monitoring_section}
{version_section}

## 📝 Notes
- Any additional important information
- Known issues or limitations
- Links to related documentation
"""
    return documentation

def update_workflow_documentation():
    """Update documentation for all workflows"""
    for root, dirs, _ in os.walk(base_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        # Check if this is a workflow directory (contains a JSON file)
        if any(f.endswith('.json') for f in os.listdir(root)):
            workflow_name = os.path.basename(root)
            if workflow_name == base_dir:  # Skip root directory
                continue
                
            print(f"Updating documentation for: {workflow_name}")
            
            # Get workflow JSON
            workflow_json = get_workflow_json(root)
            if not workflow_json:
                print(f"  ⚠️ No JSON file found in {root}")
                continue
            
            # Generate documentation
            documentation = generate_documentation(workflow_name, workflow_json)
            
            # Write to README.md
            readme_path = os.path.join(root, 'README.md')
            with open(readme_path, 'w') as f:
                f.write(documentation)
            print(f"  ✅ Updated {readme_path}")

if __name__ == "__main__":
    update_workflow_documentation()
    print("\nDocumentation update complete!")
