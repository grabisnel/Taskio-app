import Image from "next/image";
import styles from "./page.module.css";
import Link from "next/link";
import { Button, ThemeProvider, Typography } from "@mui/material";
import { muiDarkTheme } from "@/theme/theme";
import App from "next/app";
import LoginFormView from "./Login";

export default function Home() {

  return (
    <div>
      <LoginFormView/>
    </div>
  )
}
