
function Login() {

  const handleGoogleLogin = () => {

    window.location.href =
      "http://localhost:8000/auth/login";

  };

  return (
    <div className="login-container">


      <p>Sign in to continue</p>

      <button onClick={handleGoogleLogin}>
        Continue with Google
      </button>

    </div>
  );
}

export default Login;