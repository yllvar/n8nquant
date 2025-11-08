import os
import glob
from datetime import datetime

# Categories for workflows
CATEGORIES = {
    'market': 'Market Data',
    'risk': 'Risk Management',
    'trading': 'Trading',
    'analytics': 'Analytics',
    'operations': 'Operations',
    'reporting': 'Reporting'
}

def get_workflow_info(directory):
    """Extract workflow information from README.md"""
    readme_path = os.path.join(directory, 'README.md')
    if not os.path.exists(readme_path):
        return None
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Extract workflow name from directory name
    workflow_name = os.path.basename(directory)
    
    # Extract description (first paragraph after the first heading)
    description = ""
    lines = content.split('\n')
    in_description = False
    
    for line in lines:
        if line.startswith('## '):
            if in_description:
                break
            in_description = True
            continue
        if in_description and line.strip():
            description = line.strip()
            break
    
    # Determine category based on directory name
    category = 'Other'
    for key, value in CATEGORIES.items():
        if key in directory.lower():
            category = value
            break
    
    return {
        'name': workflow_name,
        'description': description,
        'category': category,
        'path': directory
    }

def update_root_readme():
    """Update the root README.md with workflow catalog"""
    # Find all workflow directories (those containing a README.md)
    workflow_dirs = [d for d in glob.glob('*') 
                    if os.path.isdir(d) and os.path.exists(os.path.join(d, 'README.md'))]
    
    # Get workflow information
    workflows = []
    for dir_path in workflow_dirs:
        info = get_workflow_info(dir_path)
        if info:
            workflows.append(info)
    
    # Sort workflows by category and name
    workflows.sort(key=lambda x: (x['category'], x['name']))
    
    # Generate workflow catalog markdown
    catalog = ""
    current_category = None
    for i, workflow in enumerate(workflows, 1):
        if workflow['category'] != current_category:
            if current_category is not None:
                catalog += "|"
            current_category = workflow['category']
            catalog += f"\n### {current_category}\n\n"
            catalog += "| # | Workflow | Description | Documentation |\n"
            catalog += "|---|----------|-------------|----------------|\n"
        
        # Create relative path for documentation
        rel_path = os.path.join(workflow['path'], 'README.md')
        catalog += f"| {i} | {workflow['name']} | {workflow['description']} | [View Documentation]({rel_path}) |\n"
    
    # Read current README
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Update the workflow catalog section
    start_marker = '## 📋 Workflow Catalog\n'
    end_marker = '## 🚀 Quick Start Guide'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx + len(start_marker)]
        new_content += "\n" + catalog + "\n"
        new_content += content[end_idx:]
        
        # Write updated content
        with open('README.md', 'w') as f:
            f.write(new_content)
        
        print("✅ Successfully updated root README.md")
    else:
        print("⚠️ Could not find workflow catalog section in README.md")

if __name__ == "__main__":
    update_root_readme()
