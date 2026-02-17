import React, { useState } from "react";
import Button from "./components/Button";

function App() {
  const [loadingBtn, setLoadingBtn] = useState(null);

  const handleLoadingDemo = (id) => {
    setLoadingBtn(id);
    setTimeout(() => setLoadingBtn(null), 2000);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-16 px-4">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-900 mb-2 text-center">
          Button Component
        </h1>
        <p className="text-gray-500 text-center mb-12">
          A reusable, accessible React button with multiple variants, sizes, and
          states.
        </p>

        {/* Variants */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
            Variants
          </h2>
          <div className="flex flex-wrap gap-4 items-center">
            <Button variant="primary">Primary</Button>
            <Button variant="secondary">Secondary</Button>
            <Button variant="outline">Outline</Button>
            <Button variant="ghost">Ghost</Button>
            <Button variant="danger">Danger</Button>
          </div>
        </section>

        {/* Sizes */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Sizes</h2>
          <div className="flex flex-wrap gap-4 items-center">
            <Button size="sm">Small</Button>
            <Button size="md">Medium</Button>
            <Button size="lg">Large</Button>
          </div>
        </section>

        {/* Disabled */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
            Disabled State
          </h2>
          <div className="flex flex-wrap gap-4 items-center">
            <Button variant="primary" disabled>
              Primary Disabled
            </Button>
            <Button variant="outline" disabled>
              Outline Disabled
            </Button>
            <Button variant="danger" disabled>
              Danger Disabled
            </Button>
          </div>
        </section>

        {/* Loading */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
            Loading State
          </h2>
          <p className="text-sm text-gray-500 mb-3">
            Click a button to see the loading spinner for 2 seconds.
          </p>
          <div className="flex flex-wrap gap-4 items-center">
            <Button
              variant="primary"
              loading={loadingBtn === "primary"}
              onClick={() => handleLoadingDemo("primary")}
            >
              Submit
            </Button>
            <Button
              variant="secondary"
              loading={loadingBtn === "secondary"}
              onClick={() => handleLoadingDemo("secondary")}
            >
              Processing
            </Button>
            <Button
              variant="danger"
              loading={loadingBtn === "danger"}
              onClick={() => handleLoadingDemo("danger")}
            >
              Deleting
            </Button>
          </div>
        </section>

        {/* Full Width */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
            Full Width
          </h2>
          <div className="flex flex-col gap-4">
            <Button variant="primary" fullWidth>
              Full Width Primary
            </Button>
            <Button variant="outline" fullWidth>
              Full Width Outline
            </Button>
          </div>
        </section>

        {/* Mixed Combinations */}
        <section className="mb-12">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
            Combinations
          </h2>
          <div className="flex flex-wrap gap-4 items-center">
            <Button variant="primary" size="sm">
              Small Primary
            </Button>
            <Button variant="outline" size="lg">
              Large Outline
            </Button>
            <Button variant="danger" size="sm" disabled>
              Small Danger Disabled
            </Button>
            <Button variant="ghost" size="lg">
              Large Ghost
            </Button>
          </div>
        </section>
      </div>
    </div>
  );
}

export default App;
