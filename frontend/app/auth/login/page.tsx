'use client'

import { useActionState } from 'react'
import { login } from '../../action'
import AuthRedirect from '../../components/AuthRedirect'

export default function LoginPage() {
  const [state, formAction, isPending] = useActionState(login, { error: null })

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-stone-800 rounded-lg shadow-md">
      <h1 className="text-2xl font-bold mb-6 text-center">Login</h1>

      <form action={formAction} className="space-y-4">
        <div>
          <label className="block text-sm font-medium">Username</label>
          <input 
            name="username" 
            type="text" 
            required 
            className="w-full border p-2 rounded focus:ring-2 focus:ring-blue-500 outline-none" 
          />
        </div>

        <div>
          <label className="block text-sm font-medium">Password</label>
          <input 
            name="password" 
            type="password" 
            required 
            className="w-full border p-2 rounded focus:ring-2 focus:ring-blue-500 outline-none" 
          />
        </div>

        {state?.error && (
          <p className="text-red-500 text-sm font-medium">{state.error}</p>
        )}

        <button
          type="submit"
          disabled={isPending}
          className="w-full bg-stone-700 text-red-800 hover:text-red-500 disabled:bg-gray-400 transition-colors"
        >
          {isPending ? 'Logging in...' : 'Login'}
        </button>
      </form>

      <AuthRedirect type="login" />
    </div>
  )
}