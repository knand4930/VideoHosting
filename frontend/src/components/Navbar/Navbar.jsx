import React from "react";
import "./Navbar.css";
import { Link, useNavigate } from "react-router-dom";
import GtmLogo from "../../assets/Rectangle 2.png";
import { useDispatch, useSelector } from "react-redux";
import { setSessionUser } from "../../slices/sessionSlice";
import axios from "axios";

function Navbar() {
  const { sessionUser } = useSelector((state) => state.sessionSlice);

  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleLogout = async () => {
    await axios.get(`/api/session/logout`);
    dispatch(setSessionUser({}));
    navigate("/login");
  };

  const Options = () => {
    return (
      <div className="navbar-options">
        {/* <Link to="/"> Home </Link> */}

        {sessionUser && sessionUser.email ? (
          <>
            <Link to="/dashboard">Dashboard</Link>
            <span className="loginButtonNAv" onClick={handleLogout}>
              Logout
            </span>
          </>
        ) : (
          <Link to="/login" className="loginButtonNAv">
            Login / Signup
          </Link>
        )}
      </div>
    );
  };

  return (
    <div className="navbar">
      <img src={GtmLogo} alt="" />
      <Options />
    </div>
  );
}

export default Navbar;
