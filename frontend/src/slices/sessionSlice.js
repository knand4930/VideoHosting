import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export const sessionSlice = createSlice({
  name: "session",
  initialState: {
    sessionUser: {},
    error: "",
  },
  reducers: {
    setSessionUser: (state, action) => {
      const { payload } = action;
      state.sessionUser = payload;
    },
  },
});

// Export Actions
export const { setSessionUser } = sessionSlice.actions;

// Export Reducer
export default sessionSlice.reducer;
