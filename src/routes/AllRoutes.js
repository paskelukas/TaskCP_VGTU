import { Routes, Route } from "react-router-dom";
import { Home, MainPage, ContentImport, PidMigration, Badges, PageNotFound } from "../pages";

export const AllRoutes = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path=":client" element={<MainPage />} />
        <Route path=":client/content-import" element={<ContentImport />} />
        <Route path=":client/pid-migration" element={<PidMigration />} />
        <Route path=":client/badges" element={<Badges />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </>
  );
};
