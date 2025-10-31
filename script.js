// Signup
document.getElementById('signupForm')?.addEventListener('submit', function(e) {
  e.preventDefault();
  
  const id = document.getElementById('universityId').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  localStorage.setItem('user', JSON.stringify({ id, email, password }));
  alert('Account created! Redirecting to profile setup...');
  window.location.href = 'profile.html';
});

// Login
document.getElementById('loginForm')?.addEventListener('submit', function(e) {
  e.preventDefault();
  
  const id = document.getElementById('loginId').value;
  const password = document.getElementById('loginPassword').value;
  const user = JSON.parse(localStorage.getItem('user'));

  if (user && user.id === id && user.password === password) {
    alert('Login successful!');
    window.location.href = 'profile.html';
  } else {
    alert('Invalid login credentials.');
  }
});

// Profile creation
document.getElementById('profileForm')?.addEventListener('submit', function(e) {
  e.preventDefault();
  
  const profile = {
    name: document.getElementById('name').value,
    university: document.getElementById('university').value,
    major: document.getElementById('major').value,
    modules: document.getElementById('modules').value,
    goals: document.getElementById('goals').value,
    studyTime: document.getElementById('studyTime').value
  };
  
  localStorage.setItem('profile', JSON.stringify(profile));
  alert('Profile saved successfully!');
  window.location.href = 'dashboard.html'; // or next page
});
