import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  rewrites: async () => {
    return [
      {
        source: '/backend/:path*',
        destination: process.env.NODE_ENV === 'development'
          ? '127.0.0.1*'
          : '/backend/',
      },
    ];
  },
};

export default nextConfig;
