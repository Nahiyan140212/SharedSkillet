import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Recipes from "./pages/Recipes";
import GenerateRecipe from "./pages/GenerateRecipe";
import OrderTracker from "./components/OrderTracker";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <header className="bg-orange-600 text-white p-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold">SharedSkillet 🍳</h1>
          <nav>
            <a href="/" className="text-white mr-4 hover:underline">Home</a>
            <a href="/recipes" className="text-white mr-4 hover:underline">Recipes</a>
            <a href="/generate" className="text-white mr-4 hover:underline">Generate Recipe</a>
            <a href="/orders" className="text-white hover:underline">Orders</a>
          </nav>
        </header>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/recipes" element={<Recipes />} />
          <Route path="/generate" element={<GenerateRecipe />} />
          <Route path="/orders" element={<OrderTracker />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;