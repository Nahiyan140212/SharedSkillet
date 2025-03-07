# SharedSkillet
Here is our initial MVP:  [Shared Skillet](https://SharedSkillet.com) 


*This is just the beginning! Excited to build this AI-powered recipe platform!* 

---

## AI-Powered Recipe Platform with Image Recognition & Food Delivery  

🚀 **SharedSkillet** is a smart recipe platform that lets users:  
1. Upload food images to get AI-generated recipe suggestions  
2. Generate grocery lists based on recognized ingredients  
3. Order prepared meals within 50 miles  
4. Watch step-by-step cooking videos  

---

##  Features
-  **Food Image Recognition**: Upload a picture, and AI finds the best matching recipe.
-  **Recipe Generation**: Get auto-generated step-by-step instructions.
-  **Grocery List Generator**: AI extracts ingredients for easy shopping.
-  **On-Demand Food Delivery**: Order meals if you’re within 50 miles.
-  **Step-by-Step Video Guides**: Watch how meals are prepared.
-  **Multilingual Support**: Recipes available in multiple languages.

---

## Tech Stack
**Frontend:** React.js 
**Backend:** Flask / FastAPI (Python)  
**Database:** PostgreSQL / DynamoDB  
**AI/ML:** Amazon Rekognition + AWS Bedrock (LLM)  
**Cloud Hosting:** AWS (S3, Lambda, CloudFront, API Gateway)  
**Payments:** Stripe / Amazon Pay  

---
## 📂 Backend Folder Structure _(Updated: March 8, 2024)_

# 📂 SharedSkillet - Project Structure

```plaintext
SharedSkillet/
├── backend/                 # Backend service (FastAPI, AI, Payments, Database)
│   ├── app/                 # Core application logic
│   │   ├── main.py          # FastAPI main entry point
│   │   ├── models.py        # Database models (SQLAlchemy/DynamoDB)
│   │   ├── ai.py            # AI-powered recipe generation (GPT-4 integration)
│   │   ├── database.py      # Database connection setup
│   │   └── payments.py      # Payment processing (Stripe integration)
│   ├── lambda_handler.py    # AWS Lambda handler for serverless execution
│   ├── requirements.txt     # Python dependencies
│   └── template.yaml        # AWS SAM template for deployment
├── frontend/                # React (TypeScript) frontend
│   ├── src/                 # Frontend source code
│   │   ├── components/      # Reusable React components
│   │   ├── pages/           # Page-level components (Home, Recipes, Orders)
│   │   ├── services/        # API service calls (Axios, Cognito Auth)
│   │   ├── App.tsx          # Main app component
│   │   ├── index.tsx        # React entry point
│   │   └── tailwind.config.js  # TailwindCSS configuration
│   ├── public/              # Static assets (HTML, images, icons)
│   ├── package.json         # Node.js dependencies & scripts
│   └── tsconfig.json        # TypeScript configuration
├── infra/                   # Infrastructure as Code (AWS CDK, deployment scripts)
│   ├── cdk/                 # AWS CDK resources for infrastructure provisioning
│   └── deploy.sh            # Deployment script
├── data/                    # Dataset storage (recipes, user data)
│   └── recipes.csv          # CSV file containing recipe dataset
├── docs/                    # Documentation & progress tracking
│   └── progress.md          # Development progress & notes
├── .gitignore               # Ignore unnecessary files in Git
└── README.md                # Project documentation

```


The **frontend** built using **React (TypeScript), TailwindCSS, and AWS services**.

---

## 📂 Frontend Folder Structure _(Updated: March 8, 2024)_

```plaintext
frontend/
├── src/                    # React application source code
│   ├── components/         # Reusable React components
│   │   ├── RecipeCard.tsx  # Component for recipe display
│   │   ├── SearchBar.tsx   # Component for search input
│   │   ├── OrderForm.tsx   # Component for order placement
│   │   ├── Header.tsx      # Header with logo
│   │   └── RecipeGenerator.tsx  # Component for AI recipe generation and image-to-recipe
│   ├── pages/              # Page-level components
│   │   ├── Home.tsx        # Replaces index.html
│   │   ├── Recipes.tsx     # Replaces recipes1.html to recipes4.html
│   │   └── Orders.tsx      # Order tracking page
│   ├── services/           # API service calls
│   │   ├── api.ts          # Axios-based API calls to FastAPI
│   │   └── auth.ts         # Cognito authentication
│   ├── App.tsx             # Main app component
│   ├── index.tsx           # Entry point
│   └── tailwind.config.js  # Tailwind CSS configuration
├── public/                 # Static assets (served by React or S3)
│   ├── index.html          # Fallback HTML (loads React app)
│   ├── recipes1.html       # Existing static recipe page 1
│   ├── recipes2.html       # Existing static recipe page 2
│   ├── recipes3.html       # Existing static recipe page 3
│   ├── recipes4.html       # Existing static recipe page 4
│   ├── logo.png            # Project logo
│   ├── cooking-hero.jpg    # Hero image
│   └── favicon.ico         # Favicon (optional)
├── package.json            # Node.js dependencies and scripts
└── tsconfig.json           # TypeScript configuration

```


Updated by: [Nahiyan Bin Noor](https://github.com/Nahiyan140212)
- 