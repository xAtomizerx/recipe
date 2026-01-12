import Image from "next/image";

export default async function Home() {
  // 1. Point to your FastAPI backend URL (from Environment Variables)
  // Use a fallback for local development
  const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

  let backendStatus = "Checking...";

  try {
    const response = await fetch(`${API_URL}/`, { 
      cache: 'no-store' // Ensures you get a fresh status on every visit
    });
    
    if (response.ok) {
      const data = await response.json();
      backendStatus = data.message; // "Welcome to the Recipe API" from your main.py
    } else {
      backendStatus = "Backend is online but returned an error.";
    }
  } catch (error) {
    backendStatus = "Backend is currently unreachable.";
  }

  return (
    <>Welcome to Recipe App</>
  );
}
