import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  rewrites: async () => {
    return [
      {
        source: '/backend/:path*',
        destination: process.env.NODE_ENV === 'development'
          ? 'http://localhost:8000/: path*'
          : '/backend/',
           
      },
    ];
  },
  experimental: {
    serverActions: {
      allowedOrigins: [
        "localhost:3000",
        "special-goggles-r4qjq6gwv67g3p4-3000.app.github.dev",
        // You can also use a wildcard for all github.dev subdomains if needed
        "*.app.github.dev",
        "recipe-4sku.vercel.app",
        "recipe-4sku-nl5xyu85j-atomizers-projects.vercel.app",
      ],
    },
  }
};

export default nextConfig;
