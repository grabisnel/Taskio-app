import { setAuthHeaderToken } from "./auth-api.service"

const AUTH_TOKEN_STORAGE_KEY = "taskio_auth_token"

export function saveAuthToken(token: string) {
    if (typeof window !== "undefined") {
        localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, token)
    }

    setAuthHeaderToken(token)
}

export function clearSavedAuthToken() {
    if (typeof window !== "undefined") {
        localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
    }

    setAuthHeaderToken(null)
}

export function loadSavedAuthToken() {
    if (typeof window === "undefined") {
        return null
    }

    const token = localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)

    if (token) {
        setAuthHeaderToken(token)
    }

    return token
}