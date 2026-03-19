import { StyledLoginContainer } from "./login-container.styles"

export const LoginContainer = ({ children }: { children: React.ReactNode }) => {
    return (
        <StyledLoginContainer>
            {children}
         </StyledLoginContainer>)
}
