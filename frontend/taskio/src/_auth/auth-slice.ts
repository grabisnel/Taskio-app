import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AuthState, User } from "./types/auth-slice.types";



const initialState: AuthState = {
    user: null,
    loading: false,
    isAuthenticated: false
}


const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        startLoading(state) {

            state.loading = true
        },
        setUser(state, action: PayloadAction<User>) {
            state.user = action.payload;
            state.isAuthenticated = true;
            state.loading = false;
        },
        clearUser(state) {
            state.user = null;
            state.isAuthenticated = false;
            state.loading = false;
        }



    }

})

export const { startLoading, setUser, clearUser } = authSlice.actions;
export default authSlice.reducer




