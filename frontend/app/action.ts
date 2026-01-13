'use server'

import { redirect } from 'next/navigation'
import { cookies } from 'next/headers'

// Define your FastAPI production URL (ideally use an environment variable)
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function signup(prevState: any, formData: FormData) {
  const username = formData.get('username');
  const email = formData.get('email');
  const password = formData.get('password');

  // Change: Fetch to your FASTAPI backend, not Supabase directly
  const response = await fetch(`${API_URL}auth/signup`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password }),
  });

  const result = await response.json();

  if (!response.ok) {
    return { error: result.detail || "Signup failed." };
  }

  redirect('/login');
}

export async function login(prevState: any, formData: FormData) {
  const username = formData.get('username');
  const password = formData.get('password');

  const authData = new URLSearchParams();
  authData.append('username', username as string);
  authData.append('password', password as string);

  // Change: Fetch to your FASTAPI backend /token endpoint
  const response = await fetch(`${API_URL}auth/token`, {
    method: 'POST',
    body: authData,
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });

  const result = await response.json();

  if (!response.ok) {
    return { error: result.detail || "Invalid username or password" };
  }

  const cookieStore = await cookies();
  cookieStore.set('access_token', result.access_token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 20, 
  });

  redirect('/recipes');
}