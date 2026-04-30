
import { createTheme } from '@mui/material/styles';
import { colorTokens } from '../tokens/tokens';



const theme = createTheme({
  palette: {
    primary: {
      main: colorTokens.primary.main,
      contrastText: colorTokens.primary.contrastText,
    },
    background: {
      default: colorTokens.background.default,
      paper: colorTokens.background.paper,
    },
    text: {
      primary: colorTokens.text.primary,
      secondary: colorTokens.text.secondary,
    },
    divider: colorTokens.divider,
    neutral: {
      ...colorTokens.neutral,
    } as any,
  },
  shape: {
    borderRadius: 10,
  },
});

export default theme;
