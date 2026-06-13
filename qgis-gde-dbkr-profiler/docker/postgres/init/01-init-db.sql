-- Creates small sample data so local profiling can exercise PostgreSQL immediately.
CREATE TABLE IF NOT EXISTS public.sample_assets (
    id SERIAL PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    asset_type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO public.sample_assets (asset_name, asset_type)
VALUES
    ('Road Segment A', 'road'),
    ('Building Block B', 'building'),
    ('Parcel Sheet C', 'parcel'),
    ('Network Link D', 'network')
ON CONFLICT DO NOTHING;
