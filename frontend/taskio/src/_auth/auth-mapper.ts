import { BackendUserResponse } from "./types/auth-service.types";
import { User } from "./types/auth-slice.types";

export function mapUserResponseToAuthUser(data: BackendUserResponse): User {
    return {
        username: data.username ?? "",
        email: data.email ?? "",
        first_name: data.first_name ?? "",
        last_name: data.last_name ?? "",
    }
}