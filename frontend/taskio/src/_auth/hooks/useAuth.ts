import { AppDispatch, RootState } from "@/stores/app-store";
import { useDispatch, useSelector } from "react-redux";
import { clearUser, setUser, startLoading } from "../auth-slice";
import {
	getCurrentUser,
	login as loginService,
	logout as logoutService,
} from "../services/auth.service";


export function useAuth() {
	const dispatch = useDispatch<AppDispatch>();
	const { user, loading, isAuthenticated } = useSelector((state: RootState) => state.auth);

	async function login(username: string, password: string) {

		dispatch(startLoading());

		try {
			await loginService({ username, password });
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