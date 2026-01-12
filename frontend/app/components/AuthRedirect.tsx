
import Link from 'next/link';

interface AuthRedirectProps {
  type: 'login' | 'signup';
}

export default function AuthRedirect({ type }: AuthRedirectProps) {
  const isLogin = type === 'login';

  return (
    <div className="mt-6 text-center text-sm text-gray-600 items-center">
      <p>
        {isLogin ? "Don't have an account?" : "Already have an account?"}
        <Link 
          href={isLogin ? "/signup" : "/login"}
          className="ml-1 font-semibold text-red-900 hover:text-red-500 transition-colors"
        >
          {isLogin ? "Sign Up here" : "Log In here"}
        </Link>
      </p>
    </div>
  );
}