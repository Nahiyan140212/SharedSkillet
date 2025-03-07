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


The **frontend** built using **React (TypeScript), TailwindCSS, and AWS services**.

---

## 📂 Frontend Folder Structure _(Updated: March 8, 2024)_

```plaintext
frontend/
├── src/                    
│   ├── components/         # Reusable React components
│   │   ├── RecipeCard.tsx  # Displays recipes dynamically
│   │   ├── SearchBar.tsx   # Search bar for filtering recipes
│   │   ├── OrderForm.tsx   # Order placement form
│   │   └── Header.tsx      # App header with navigation & logo
│   ├── pages/              # Page-level React components
│   │   ├── Home.tsx        # Homepage (Replaces index.html)
│   │   ├── Recipes.tsx     # AI-generated recipes display
│   │   └── Orders.tsx      # Order tracking page
│   ├── services/           # API service calls (FastAPI integration)
│   │   ├── api.ts          # Handles API requests using Axios
│   │   └── auth.ts         # AWS Cognito authentication
│   ├── App.tsx             # Main app component (Routing)
│   ├── index.tsx           # Entry point for React app
│   └── tailwind.config.js  # Tailwind CSS configuration
├── public/                 # Static assets (served via React or S3)
│   ├── index.html          # Fallback HTML page
│   ├── recipes1.html       # Legacy static recipe page 1
│   ├── recipes2.html       # Legacy static recipe page 2
│   ├── recipes3.html       # Legacy static recipe page 3
│   ├── recipes4.html       # Legacy static recipe page 4
│   ├── logo.png            # Project logo
│   ├── cooking-hero.jpg    # Homepage hero image
│   └── favicon.ico         # Browser icon (optional)
├── package.json            # Node.js dependencies & scripts
└── tsconfig.json           # TypeScript configuration

```

Updated by: [Nahiyan Bin Noor](https://github.com/Nahiyan140212)
- 