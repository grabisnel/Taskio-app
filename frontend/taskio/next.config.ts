import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  allowedDevOrigins: [
    "http://192.168.1.19:3000",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
  ]
};

module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: `${process.env.DJANGO_API_URL}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
