'use server'

import { BackendUserResponse } from "./types/auth-service.types";
import { User } from "./types/auth-slice.types";

export async function mapUserResponseToAuthUser(data: BackendUserResponse): Promise<User> {
    return {
        username: data.username ?? "",
        email: data.email ?? "",
        first_name: data.first_name ?? "",
        last_name: data.last_name ?? "",
    }
}