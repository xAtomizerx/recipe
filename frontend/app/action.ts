'use server'

import { redirect } from 'next/navigation'

// Ensure the function name is 'signup' and it accepts (prevState, formData)
export async function signup(prevState: any, formData: FormData) {
  const username = formData.get('username')
  const email = formData.get('email')
  const password = formData.get('password')

  const response = await fetch('https://recipe-9811nf6hf-atomizers-projects.vercel.app/backend/auth/signup', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password }),
  })

  const result = await response.json()

  if (!response.ok) {
    return { error: result.detail || "Signup failed." }
  }

  redirect('/login')
}

import { cookies } from 'next/headers'

export async function login(prevState: any, formData: FormData) {
  const username = formData.get('username')
  const password = formData.get('password')

  // FastAPI expects OAuth2 password flow (Form Data, not JSON)
  const authData = new URLSearchParams()
  authData.append('username', username as string)
  authData.append('password', password as string)

  const response = await fetch('https://recipe-9811nf6hf-atomizers-projects.vercel.app/auth/token', {
    method: 'POST',
    body: authData,
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  })

  const result = await response.json()

  if (!response.ok) {
    return { error: result.detail || "Invalid username or password" }
  }

  // Store JWT in a secure, HttpOnly cookie
  const cookieStore = await cookies()
  cookieStore.set('access_token', result.access_token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 20, // 20 minutes (matches your backend token expiry)
  })

  redirect('/recipes') // Send user to the recipes dashboard
}