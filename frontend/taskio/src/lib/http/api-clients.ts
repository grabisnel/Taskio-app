import { createApiClient } from "./create-api-client"
import { getSavedAuthToken } from "@/_auth/services/auth-token.storage"

export const authApi = createApiClient("auth", getSavedAuthToken)
export const userApi = createApiClient("user", getSavedAuthToken)
