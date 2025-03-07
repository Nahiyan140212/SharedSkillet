import React, { useState } from "react";
import axios from "axios";

interface Recipe {
  title: string;
  ingredients: string[];
  instructions: string;
  public_url: string;
}

const RecipeGenerator: React.FC = () => {
  const [ingredients, setIngredients] = useState<string>("");
  const [image, setImage] = useState<File | null>(null);
  const [recipe, setRecipe] = useState<Recipe | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Generate recipe from ingredients
  const generateRecipe = async () => {
    setLoading(true);
    setError(null);
    try {
      const token = localStorage.getItem("token") || ""; // Replace with Cognito token
      const response = await axios.post(
        "https://your-api-gateway-url/api/recipes/generate",
        { ingredients },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setRecipe(response.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to generate recipe.");
    } finally {
      setLoading(false);
    }
  };

  // Generate recipe from image upload
  const analyzeImage = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setImage(file);
      setLoading(true);
      setError(null);
      try {
        const token = localStorage.getItem("token") || "";
        const formData = new FormData();
        formData.append("file", file);
        const response = await axios.post(
          "https://your-api-gateway-url/api/recipes/image",
          formData,
          {
            headers: {
              Authorization: `Bearer ${token}`,
              "Content-Type": "multipart/form-data",
            },
          }
        );
        setRecipe(response.data);
      } catch (err: any) {
        setError(err.response?.data?.detail || "Failed to analyze image.");
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="recipe-generator p-6 max-w-5xl mx-auto mt-20">
      <h2 className="text-2xl font-bold text-orange-600 text-center mb-4">
        Generate a Recipe
      </h2>
      {/* Input for ingredients */}
      <div className="mb-4">
        <label className="block text-gray-700 mb-2">Enter Ingredients</label>
        <input
          type="text"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          placeholder="e.g., chicken, rice, tomatoes"
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-orange-600"
        />
        <button
          onClick={generateRecipe}
          disabled={loading}
          className={`mt-2 w-full p-2 rounded text-white ${
            loading ? "bg-gray-400 cursor-not-allowed" : "bg-orange-600 hover:bg-orange-700"
          } transition-colors`}
        >
          {loading ? "Generating..." : "Generate Recipe"}
        </button>
      </div>
      {/* Image upload */}
      <div className="mb-4">
        <label className="block text-gray-700 mb-2">Upload Food Image</label>
        <input
          type="file"
          accept="image/*"
          onChange={analyzeImage}
          className="w-full p-2 border rounded"
        />
      </div>
      {/* Error message */}
      {error && (
        <p className="text-red-500 text-center mb-4">{error}</p>
      )}
      {/* Generated recipe display */}
      {recipe && (
        <div className="recipe-result p-4 border rounded bg-white shadow-md">
          <h3 className="text-xl font-semibold text-orange-600">{recipe.title}</h3>
          <p className="mt-2"><strong>Ingredients:</strong> {recipe.ingredients.join(", ")}</p>
          <p className="mt-2"><strong>Instructions:</strong> {recipe.instructions}</p>
          {recipe.public_url && (
            <iframe
              src={recipe.public_url.replace("view", "preview")}
              allow="autoplay"
              loading="lazy"
              className="w-full h-48 border-none mt-2"
            ></iframe>
          )}
        </div>
      )}
    </div>
  );
};

export default RecipeGenerator;