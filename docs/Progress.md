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
- [Nahiyan Bin Noor](https://github.com/Nahiyan140212)

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

 # Shared Skillet Website Development Documentation - March 8, 2025

## Overview
This document outlines the steps taken to develop and enhance the `sharedskillet.com` website, hosted on Amazon S3 with Route 53. The work was completed with guidance from Grok 3, an AI assistant by xAI, to create a professional-looking recipe-sharing platform.

## Tasks Completed Today

### 1. Initial Setup and Data Analysis
- **Analyzed `Complete.csv`**: Loaded and inspected a CSV file containing recipe data (e.g., `File Name`, `Title`, `Public URL`, `Recipe in Plain text`) with 103 rows.
- **Fixed Script Error**: Resolved an `argument of type 'float' is not iterable` error caused by `NaN` values in `Public URL` by adding `pd.notna()` checks in the Jupyter Notebook script.
- **Generated HTML**: Created a basic `recipes.html` file with embedded Google Drive video iframes using a Jupyter script.

### 2. Website Structure and Styling
- **Created `index.html`**: Designed a homepage with a hero section, navigation, and business plan popup, using responsive CSS with Flexbox and media queries.
- **Developed `recipes.html`**: Built a recipe page with a grid layout for 103 video cards, adding responsiveness for mobile and desktop browsers.
- **Added Logo and Name**: Integrated a `logo.png` file and displayed "Shared Skillet 🍳" alongside it in the header of both `index.html` and `recipes.html`.
- **Engaging Image**: Replaced the Unsplash API background with a static image (`cooking-hero.jpg`) from `https://unsplash.com/photos/person-cutting-vegetables-with-knife-yWG-ndhxvqY` on the homepage.

### 3. Pagination and Performance Optimization
- **Paginated Recipes**: Reduced load time by splitting 40 videos into 8 pages (5 videos each) using a Jupyter script, generating `recipes1.html` to `recipes8.html`.
- **Added Search Bar**: Implemented a client-side search bar in recipe pages to filter by title and description.
- **Adjusted Pagination**: Later modified to 10 videos per page (4 pages: `recipes1.html` to `recipes4.html`) to balance content and performance.
- **Fixed Path Issue**: Corrected an `[Errno 22] Invalid argument` error by using `os.makedirs` and `os.path.join` to save files to `..\frontend`, ensuring proper directory handling.

### 4. Deployment to S3
- **Uploaded Files**: Deployed `index.html`, `recipes.html` (later replaced by paginated files), `logo.png`, and `cooking-hero.jpg` to the `sharedskillet.com` S3 bucket.
- **Made Public**: Ensured all files were publicly accessible via ACL settings in the AWS Console.
- **Tested URLs**: Verified functionality at `http://sharedskillet.com.s3-website-us-east-1.amazonaws.com/index.html` and recipe page URLs.

### 5. Troubleshooting and Enhancements
- **Slow Page Fix**: Addressed slow loading of 40 videos by implementing pagination and `loading="lazy"` for iframes.
- **HTTPS Discussion**: Explored enabling HTTPS using Amazon CloudFront and AWS Certificate Manager, though not implemented today.
- **Responsiveness**: Confirmed mobile and desktop compatibility with media queries and flexible layouts.

## Tools and Technologies Used
- **Python**: Jupyter Notebook for script development and HTML generation.
- **Pandas**: For CSV data manipulation.
- **HTML/CSS**: For website structure and styling.
- **AWS S3**: For static hosting.
- **AWS Route 53**: For DNS management.
- **Unsplash**: For sourcing the engaging hero image.

## Next Steps
- **Implement HTTPS**: Set up CloudFront and ACM for secure `https://sharedskillet.com`.
- **Global Search**: Add server-side search across all recipe pages.
- **ML Integration**: Explore AI-powered recipe suggestions or image analysis.
- **Performance Monitoring**: Use PageSpeed Insights to further optimize load times.

## Notes
- Ensure `..\data\Complete.csv` and `..\frontend` paths are valid relative to the script location.
- Keep `logo.png` and `cooking-hero.jpg` in the S3 bucket (e.g., root or `images/` folder) and update paths if necessary.
- Regularly test responsiveness and video loading on different devices.

📂 Project Folder Structure (Updated)
SharedSkillet/
├── backend/         # API and backend logic
│   └── __init__.py
├── frontend/        # Frontend UI code (HTML files)
│   ├── recipes1.html
│   ├── recipes2.html
│   ├── recipes3.html
│   ├── recipes4.html
│   └── placeholder.txt
├── infra/           # AWS infrastructure setup
│   └── placeholder.txt
├── data/            # Recipe dataset (JSON, images)
│   └── Complete.csv
├── scripts/         # Deployment scripts
│   └── deploy.sh
├── docs/            # Documentation
│   └── progress.md
├── .gitignore       # Ignore unnecessary files
└── .git/            # Git repository metadata

---

## Day 3 Tasks Completed - March 7, 2025
### 🌐 1. Implement HTTPS with CloudFront and ACM
HTTPS secures the `sharedskillet.com` site with an SSL/TLS certificate, enhancing user trust, data protection, and SEO performance.

#### Currently we have
- An AWS account with access to S3, Route 53, CloudFront, and ACM.
- The S3 bucket (`sharedskillet.com`) contains `index.html`, `recipes1.html` to `recipes4.html`, `logo.png`, and `cooking-hero.jpg`.
- Route 53 is configured as the DNS provider for `sharedskillet.com`.


#### Steps Completed
1. **Request an SSL Certificate in ACM**:
   - **Action**: Navigated to the AWS Management Console > Certificate Manager (ACM).
   - **Process**: Clicked "Request a certificate" > Selected "Request a public certificate" > Entered `sharedskillet.com` and `*.sharedskillet.com` (for subdomains).
   - **Validation**: Chose DNS validation > Proceeded to generate CNAME records provided by ACM.
   - **Outcome**: Copied the CNAME records for DNS validation.

2. **Update Route 53 DNS Records**:
   - **Action**: Went to Route 53 > Selected the Hosted Zone for `sharedskillet.com`.
   - **Process**: Added the CNAME records from ACM under the "Records" section.
   - **Validation**: Waited for DNS validation (completed within a few hours) and confirmed the ACM certificate status as "Issued".
   - **Outcome**: DNS validation was successful, as verified in the ACM Console.

3. **Create a CloudFront Distribution**:
   - **Action**: Navigated to CloudFront > Clicked "Create Distribution".
   - **Settings**:
     - **Origin Domain**: Entered the S3 bucket website endpoint: `sharedskillet.com.s3-website-us-east-1.amazonaws.com` (obtained from S3 Properties > Static website hosting).
     - **Viewer Protocol Policy**: Set to "Redirect HTTP to HTTPS" to enforce secure connections.
     - **SSL Certificate**: Selected the ACM certificate requested for `sharedskillet.com`.
     - **Alternate Domain Names (CNAMEs)**: Added `sharedskillet.com`.
   - **Deployment**: Saved the configuration and waited approximately 10-15 minutes for deployment.
   - **Outcome**: The distribution deployed successfully, with the state changing to "Deployed" in the CloudFront Console. Noted the distribution domain (e.g., `d123456789abcd.cloudfront.net`).

4. **Update Route 53 with CloudFront Alias**:
   - **Action**: In Route 53, edited the `sharedskillet.com` A record.
   - **Process**: Changed the value to the CloudFront distribution domain (e.g., `d123456789abcd.cloudfront.net`) and selected "Alias" to Yes.
   - **Save**: Applied changes and waited for DNS propagation.
   - **Outcome**: The alias was updated, and `https://sharedskillet.com` resolved correctly.

#### Verification
- **Browser Test**: Visited `https://sharedskillet.com` and confirmed the site loaded with a padlock icon, indicating a secure HTTPS connection. All pages (e.g., `recipes1.html`) were accessible.
- **Command-Line Test**: Ran `curl https://sharedskillet.com` and verified a successful HTTP response with SSL encryption.
- **Certificate Validity**: Checked the browser’s certificate details, confirming it was issued by ACM for `sharedskillet.com` with a valid date range.

#### Cost Analysis
- **ACM Certificate**: Free to request and renew when used with CloudFront.
- **CloudFront Usage**:
  - **Data Transfer Out**: Estimated 1 GB/month at $0.085/GB = $0.085/month.
  - **HTTPS Requests**: Estimated 10,000 requests/month at $0.0075/10,000 requests = $0.0075/month.
  - **Total (Standard Pricing)**: $0.0925/month.
  - **Free Tier**: As a new AWS customer (first 12 months), the Free Tier provides 1 TB data transfer and 10 million requests, covering this usage, resulting in **$0.00/month**.
- **Notes**: Costs may increase with higher traffic; monitor with AWS Cost Explorer.

---

Deployment commands:
**Install Serverless:**
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html


**Backend**
```bash 
cd backend
sam build
sam deploy --guided

```

**Frontend**
Install Dependencies: npm install.
Run Locally: npm start.
Build for S3: npm run build > Upload build/ to S3 bucket (sharedskillet.com).
3. AWS Integration and Setup
DynamoDB
Tables:
SharedSkilletRecipes: Primary key id (String).
SharedSkilletOrders: Primary key order_id (String).
Create via AWS Console:
Go to DynamoDB > Create Table > Use defaults (Free Tier: 25 GB).
Cognito
Set Up User Pool:
AWS Console > Cognito > Create User Pool.
Enable email verification, OAuth2 flows, and JWT tokens.
Free Tier: 50,000 MAUs.
API Gateway
Deployed via SAM (see template.yaml).
CloudFront
Use existing distribution for S3 content.