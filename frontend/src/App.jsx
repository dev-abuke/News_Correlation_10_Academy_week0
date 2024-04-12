import { Sidebar, Navbar, LeftColumn, RightColumn } from "./components";

function App() {
  return (
    <main className="flex">
      <Sidebar />
      <div className="flex flex-col flex-1 relative">
        <Navbar />
        <div className="grid md:grid-cols-3 grid-cols-1 w-full">
          <div className="col-span-2">
            <RightColumn />
          </div>
          <div className="w-full">
            <LeftColumn />
          </div>
        </div>
      </div>
    </main>
  );
}

export default App;