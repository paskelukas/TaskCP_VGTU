import { Link } from "react-router-dom";

export const Footer = () => {
  return (
    <footer>
      <Link to="/">{new Date().getFullYear()} TaskCP &copy; Bazaarvoice</Link>
    </footer>
  );
};
