import { AppDispatch, RootState } from "@/stores/app-store";
import { useDispatch, useSelector } from "react-redux";
import { clearUser, setUser, startLoading } from "../auth-slice";
import { authApi } from "../services/auth-api";


export function useAuth() {
	const dispatch = useDispatch<AppDispatch>();
	const { user, loading, isAuthenticated } = useSelector((state: RootState) => state.auth);

	async function login(username: string, password: string) {

		dispatch(startLoading());

		await authApi.post("login/", { username, password });
		const { data } = await authApi.get("user/");

		dispatch(setUser(data));
	}

	async function logout() {

		await authApi.get("logout/");

		dispatch(clearUser());

	}

	return { user, loading, isAuthenticated, login, logout };
}