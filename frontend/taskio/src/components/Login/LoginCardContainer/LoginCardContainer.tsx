import { StyledLoginCardContainer } from "./login-card-container.styles"

export const LoginCardContainer = ({ children }: { children: React.ReactNode }) => {
    return (
        <StyledLoginCardContainer>
            {children}
        </StyledLoginCardContainer>
    )
}
