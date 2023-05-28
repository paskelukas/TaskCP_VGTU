import Migration from "../assets/migration.png";
import Import from "../assets/import.png";
import Badge from "../assets/badge.png";

import { useParams, useNavigate } from "react-router-dom";

export const MainPage = () => {
  const params = useParams();
  const navigate = useNavigate();

  return (
    <main>
      <div id="content" className="component">
        <div className="clientName">Client: {params.client}</div>
        <div className="boxes-wrapper">
          <div
            className="content-import"
            onClick={() => {
              navigate(`/${params.client}/content-import`, {
                name: params.client,
              });
            }}
          >
            <img src={Import} alt="content-import-img" />
            Content Import
          </div>
          <div
            className="product-id-migration"
            onClick={() => {
              navigate(`/${params.client}/pid-migration`);
            }}
          >
            <img src={Migration} alt="product-id-migration-img" />
            Product ID Migration
          </div>
          <div
            className="badges"
            onClick={() => {
              navigate(`/${params.client}/badges`);
            }}
          >
            <img src={Badge} alt="badges-img" />
            Badges
          </div>
        </div>
      </div>
    </main>
  );
};
