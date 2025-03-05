#  SharedSkillet Project
### AI-Powered Recipe Platform with Image Recognition & Food Delivery

*Week 1 Progress Report*  
📅 *Date: March 7, 2025*

---

##  Overview
The **SharedSkillet** project aims to create an AI-driven recipe platform that allows users to:
- Upload food images and get matching recipes  
- Generate grocery lists using AI  
- Order prepared meals (within 50 miles)  
- Access a vast collection of traditional & customized recipes  

On **Week 1**, I focused on setting up the foundation, including the **Git repository, folder structure, remote setup, and domain configuration**.

---

## Day 1 Tasks Completed
### 🛠 1️⃣ Project Initialization (Local Setup)
- Created the project directory and initialized Git  
- Structured the project with essential folders  
- Added a \`.gitignore\` file to prevent tracking unnecessary files  

\`\`\`bash
# Create project folder and initialize Git
mkdir SharedSkillet && cd SharedSkillet
git init

# Create folder structure
mkdir backend frontend infra data scripts docs
touch backend/__init__.py
touch frontend/placeholder.txt
touch infra/placeholder.txt
touch data/recipes.json
touch scripts/deploy.sh
touch docs/README.md
touch .gitignore

# First commit
git add .
git commit -m "Initial project setup"
\`\`\`

---

### 🌍 2️⃣ GitHub Repository Setup
- Linked local Git repository to **GitHub**  
- Set the default branch to \`main\`  
- Successfully pushed all initial files  

\`\`\`bash
# Add remote GitHub repository
git remote add origin https://github.com/Nahiyan140212/SharedSkillet.git
git branch -M main
git push -u origin main
\`\`\`

📌 **GitHub Repository:** [SharedSkillet on GitHub](https://github.com/Nahiyan140212/SharedSkillet.git)

---

### 🌐 3️⃣ DNS & Domain Configuration
- Configured **AWS Route 53** for domain hosting  
- Updated **Porkbun** nameservers to point to AWS  
- Verified DNS propagation with \`nslookup\`  

**Steps Taken:**
1. **Created a Public Hosted Zone** for \`sharedskillet.com\` in AWS Route 53.  
2. **Copied AWS nameservers** from Route 53.  
3. **Updated domain settings** in Porkbun to use AWS nameservers.  
4. **Tested propagation** using:
   \`\`\`bash
   nslookup sharedskillet.com
   dig sharedskillet.com NS
   \`\`\`

---

## 📂 Project Folder Structure (as of Day 1)
\`\`\`
SharedSkillet/
├── backend/         # API and backend logic
│   └── __init__.py
├── frontend/        # Frontend UI code (React/Vue)
│   └── placeholder.txt
├── infra/           # AWS infrastructure setup
│   └── placeholder.txt
├── data/            # Recipe dataset (JSON, images)
│   └── recipes.json
├── scripts/         # Deployment scripts
│   └── deploy.sh
├── docs/            # Documentation
│   └── README.md
├── .gitignore       # Ignore unnecessary files
└── .git/            # Git repository metadata
\`\`\`

---

## 🔜 Next Steps (Day 2 Plan)
 **Set up AWS S3** for storing recipe videos & static assets  
 **Decide backend framework** (Flask/Django for Python, Node.js for JavaScript)  
 **Start database design** (RDS or DynamoDB for structured data)  
 **Basic API setup** (GET /recipes, GET /recipes/:id)  

---

### 🎯 Summary
 -**Git repository initialized & pushed to GitHub**  
 -**Folder structure organized** for backend, frontend, infra, and data  
 -**Route 53 DNS configured** and domain linked to AWS  
 -**Plan defined for Day 2**  

---

### 👨‍💻 Contributors
- [Nahiyan Bin Noor](https://github.com/Nahiyan140212) (Founder & Developer)

 *This is just the beginning! Excited to build this AI-powered recipe platform!* 

---

###  How to Contribute
1. **Clone the repository**  
   \`\`\`bash
   git clone https://github.com/Nahiyan140212/SharedSkillet.git
   \`\`\`
2. **Create a new branch**  
   \`\`\`bash
   git checkout -b feature-name
   \`\`\`
3. **Commit changes & push**  
   \`\`\`bash
   git add .
   git commit -m "Added feature XYZ"
   git push origin feature-name
   \`\`\`
4. **Open a Pull Request (PR) on GitHub**  

---

 **SharedSkillet** is evolving. More features coming soon!  
 Stay tuned for more updates!  

