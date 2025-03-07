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
│   │   ├── RecipeCard.tsx  # Component for recipe display
│   │   ├── SearchBar.tsx   # Component for search input
│   │   ├── OrderForm.tsx   # Component for order placement
│   │   └── Header.tsx      # Header with logo
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
│   ├── index.html          # Fallback HTML (can redirect to React app)
│   ├── recipes1.html       # Existing static recipe page 1
│   ├── recipes2.html       # Existing static recipe page 2
│   ├── recipes3.html       # Existing static recipe page 3
│   ├── recipes4.html       # Existing static recipe page 4
│   ├── logo.png            # Project logo
│   ├── cooking-hero.jpg    # Hero image
│   └── favicon.ico         # Favicon (optional)
├── package.json            # Node.js dependencies and scripts
└── tsconfig.json           # TypeScript configuration

Updated by: [Nahiyan Bin Noor](https://github.com/Nahiyan140212)
- 