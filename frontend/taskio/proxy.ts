import { NextRequest, NextResponse } from "next/server";

export async function proxy(request: NextRequest) {
    const { pathname } = request.nextUrl;

    const token = request.cookies.get('taskio_auth_token')?.value;


    if (!token) {
        const loginUrl = new URL('/login', request.url);
        loginUrl.searchParams.set('redirectedFrom', pathname);
        return NextResponse.redirect(loginUrl);
    }

    return NextResponse.next();
}

export const config = {
    matcher: ['/tasks/:path*'],
};

