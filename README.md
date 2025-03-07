# SharedSkillet
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

**📂 Frontend Folder Structure as of March 8, 2024**
frontend/
├── src/                    # React application source code
│   ├── components/         # Reusable React components
│   │   ├── RecipeCard.tsx  # Component for displaying recipes
│   │   ├── SearchBar.tsx   # Component for searching recipes
│   │   ├── OrderForm.tsx   # Component for placing food orders
│   │   └── Header.tsx      # Header component with logo and navigation
│   ├── pages/              # Page-level components (mapped to routes)
│   │   ├── Home.tsx        # Homepage (Replaces index.html)
│   │   ├── Recipes.tsx     # AI-powered recipe page
│   │   └── Orders.tsx      # Order tracking & history
│   ├── services/           # API service calls (FastAPI integration)
│   │   ├── api.ts          # Handles Axios API calls to FastAPI
│   │   └── auth.ts         # User authentication (AWS Cognito)
│   ├── App.tsx             # Main app component (Handles routing)
│   ├── index.tsx           # Entry point for React
│   └── tailwind.config.js  # Tailwind CSS configuration
├── public/                 # Static assets (served by React or S3)
│   ├── index.html          # Fallback HTML (redirects to React)
│   ├── recipes1.html       # Legacy static recipe page 1
│   ├── recipes2.html       # Legacy static recipe page 2
│   ├── recipes3.html       # Legacy static recipe page 3
│   ├── recipes4.html       # Legacy static recipe page 4
│   ├── logo.png            # Project logo
│   ├── cooking-hero.jpg    # Homepage hero image
│   └── favicon.ico         # Browser tab icon (optional)
├── package.json            # Node.js dependencies & scripts
└── tsconfig.json           # TypeScript configuration


Updated by: [Nahiyan Bin Noor](https://github.com/Nahiyan140212)
- 