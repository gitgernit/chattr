import { User } from './User.js';

function loadClientUser(setUsers) {
  let clientUser = new User('you');
  setUsers(existing_users => [...existing_users, clientUser]);

  return () => {
    setUsers(existing_users => existing_users.filter(user => user.name !== 'you'));
  };
}

export { loadClientUser };
