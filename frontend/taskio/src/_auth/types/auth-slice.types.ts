export type User = {
    username: string;
    email: string;
    first_name: string;
    last_name: string;
}

export interface AuthState {
    user: User | null;
    loading: boolean;
    isAuthenticated: boolean;
}
