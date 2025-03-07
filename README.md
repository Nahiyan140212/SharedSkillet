# SharedSkillet
Here is our initial MVP: [Shared Skillet](https://SharedSkillet.com) 
*This is just the beginning! Excited to build this AI-powered recipe platform!* 


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
├── src/                    
│   ├── components/         
│   │   ├── RecipeCard.tsx  
│   │   ├── SearchBar.tsx   
│   │   ├── OrderForm.tsx   
│   │   └── Header.tsx      
│   ├── pages/              
│   │   ├── Home.tsx        
│   │   ├── Recipes.tsx     
│   │   └── Orders.tsx      
│   ├── services/           
│   │   ├── api.ts          
│   │   └── auth.ts         
│   ├── App.tsx             
│   ├── index.tsx           
│   └── tailwind.config.js  
├── public/                 
│   ├── index.html          
│   ├── recipes1.html       
│   ├── recipes2.html       
│   ├── recipes3.html       
│   ├── recipes4.html      
│   ├── logo.png            
│   ├── cooking-hero.jpg    
│   └── favicon.ico         
├── package.json            
└── tsconfig.json           


Updated by: [Nahiyan Bin Noor](https://github.com/Nahiyan140212)
- 