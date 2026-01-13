'use client'

import { useActionState } from 'react'
import { signup } from '../action' 

export default function SignupPage() {
  const [state, formAction, isPending] = useActionState(signup, { error: null })

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-stone-800 rounded-lg shadow-md text-white">
      <h1 className="text-2xl font-bold mb-6 text-stone-100">Create Account</h1>

      <form action={formAction} className="space-y-4">
        <div>
          <label htmlFor="username" className="block text-sm font-medium mb-1">Username</label>
          <input 
            id="username"
            name="username" 
            type="text" 
            required 
            autoComplete="username" // Added for autofill
            className="border p-2 w-full bg-stone-900 border-stone-700 rounded text-white" 
          />
        </div>

        <div>
          <label htmlFor="email" className="block text-sm font-medium mb-1">Email</label>
          <input 
            id="email"
            name="email" 
            type="email" 
            required 
            autoComplete="email" // Added for autofill
            className="border p-2 w-full bg-stone-900 border-stone-700 rounded text-white" 
          />
        </div>

        <div>
          <label htmlFor="password" className="block text-sm font-medium mb-1">Password</label>
          <input 
            id="password"
            name="password" 
            type="password" 
            required 
            autoComplete="new-password" // "new-password" is best for signup forms
            className="border p-2 w-full bg-stone-900 border-stone-700 rounded text-white" 
          />
        </div>

        {state?.error && (
          <p className="text-red-400 text-sm font-medium p-2 bg-red-900/20 rounded border border-red-900/50">
            {state.error}
          </p>
        )}

        <button
          type="submit"
          disabled={isPending}
          className="w-full bg-stone-700 text-red-500 hover:text-red-400 hover:bg-stone-600 transition-colors rounded disabled:bg-stone-800 disabled:text-stone-500 p-2 font-bold uppercase tracking-wide"
        >
          {isPending ? 'Creating Account...' : 'Sign Up'}
        </button>
      </form>
    </div>
  )
}