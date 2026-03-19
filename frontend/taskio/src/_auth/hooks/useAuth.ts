import { AppDispatch, RootState } from "@/stores/app-store";
import { useDispatch, useSelector } from "react-redux";
import { clearUser, setUser, startLoading } from "../auth-slice";
import {
	getCurrentUser,
	login as loginService,
	logout as logoutService,
} from "../services/auth.service";
import { loadSavedAuthToken } from "../services/auth-token.storage";


export function useAuth() {
	const dispatch = useDispatch<AppDispatch>();
	const { user, loading, isAuthenticated } = useSelector((state: RootState) => state.auth);

	async function login(email: string, password: string) {

		dispatch(startLoading());

		try {
			await loginService({ email, password });
			const currentUser = await getCurrentUser();

			dispatch(setUser(currentUser));
		} catch (error) {
			dispatch(clearUser());
			throw error;
		}
	}

	async function logout() {

		try {
			await logoutService();
		} finally {
			dispatch(clearUser());
		}

	}

	async function getUserSession() {
		const storedToken = loadSavedAuthToken();

		if (!storedToken) {
			return;
		}

		dispatch(startLoading());

		try {
			const currentUser = await getCurrentUser();
			dispatch(setUser(currentUser));
		} catch {
			dispatch(clearUser());
		}


	}

	return { user, loading, isAuthenticated, login, logout, getUserSession };
}