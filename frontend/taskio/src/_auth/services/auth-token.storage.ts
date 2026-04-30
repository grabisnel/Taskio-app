
const AUTH_TOKEN_STORAGE_KEY = "taskio_auth_token"

export function getSavedAuthToken(): string | null {
    if (typeof window === "undefined") return null
    return localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
}

export function saveAuthToken(token: string): void {
    if (typeof window !== "undefined") {
        localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, token)
    }
}

export function clearSavedAuthToken(): void {
    if (typeof window !== "undefined") {
        localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
    }
}

export function loadSavedAuthToken(): string | null {
    return getSavedAuthToken()
}