'use client'

import { useActionState } from 'react'
import { signup } from '../action' 

export default function SignupPage() {
  // 2. Pass 'signup' to the hook. 'formAction' is what you'll use in the <form>
  const [state, formAction, isPending] = useActionState(signup, { error: null })

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-stone-800 rounded-lg shadow-md">
      <h1 className="text-2xl font-bold mb-6">Create Account</h1>

      <form action={formAction} className="space-y-4">
        <div>
          <label className="block text-sm font-medium">Username</label>
          <input name="username" type="text" required className="border p-2 w-full" />
        </div>

        <div>
          <label className="block text-sm font-medium">Email</label>
          <input name="email" type="email" required className="border p-2 w-full" />
        </div>

        <div>
          <label className="block text-sm font-medium">Password</label>
          <input name="password" type="password" required className="border p-2 w-full" />
        </div>

        {state?.error && (
          <p className="text-red-500 text-sm">{state.error}</p>
        )}

        <button
          type="submit"
          disabled={isPending}
          className="w-full bg-stone-700 text-red-800 hover:text-red-500 rounded disabled:bg-gray-400 p-2 font-semibold"
        >
          {isPending ? 'Creating Account...' : 'Sign Up'}
        </button>
      </form>
    </div>
  )
}