import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  rewrites: async () => {
    return [
      {
        source: '/backend/:path*',
        destination: process.env.NODE_ENV === 'development'
          ? 'http://127.0.0.1:8000/*'
          : '/backend/',
           
      },
    ];
  },
  experimental: {
    serverActions: {
      allowedOrigins: [
        "localhost:3000",
        // You can also use a wildcard for all github.dev subdomains if needed
        "*.app.github.dev",
        "recipe-4sku.vercel.app",
        "https://gokvsygolwnixgyodtsi.supabase.co",
      ],
    },
  }
};

export default nextConfig;
